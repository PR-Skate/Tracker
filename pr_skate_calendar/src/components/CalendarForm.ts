import {
    AppointmentForm as AppointmentFormBase,
} from '@devexpress/dx-react-scheduler';


export namespace AppointmentForm {
    /** Properties passed to a component that renders the appointment form's overlay. */
    export type OverlayProps = AppointmentFormBase.OverlayProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders the appointment form's layout. */
    export type LayoutProps = AppointmentFormBase.LayoutProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders a layout for command buttons. */
    export type CommandLayoutProps = AppointmentFormBase.CommandLayoutProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders a layout for editors that edit basic appointment data. */
    export type BasicLayoutProps = AppointmentFormBase.BasicLayoutProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders the appointment form's layout for editors that edit the appointment's recurrence. */
    export type RecurrenceLayoutProps = AppointmentFormBase.RecurrenceLayoutProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders a Boolean value editor on the appointment form. */
    export type BooleanEditorProps = AppointmentFormBase.BooleanEditorProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders a command button on the appointment form. */
    export type CommandButtonProps = AppointmentFormBase.CommandButtonProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders a date-time editor on the appointment form. */
    export type DateEditorProps = AppointmentFormBase.DateEditorProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders a text label on the appointment form. */
    export type LabelProps = AppointmentFormBase.LabelProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders a radio group on the appointment form. */
    export type RadioGroupProps = AppointmentFormBase.RadioGroupProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders a menu of options on the appointment form. */
    export type SelectProps = AppointmentFormBase.SelectProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders a resource editor on the appointment form. */
    export type ResourceEditorProps = AppointmentFormBase.ResourceEditorProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders a text editor on the appointment form. */
    export type TextEditorProps = AppointmentFormBase.TextEditorProps;
}

export namespace AppointmentForm {
    /** Properties passed to a component that renders a weekly recurrence selector on the appointment form. */
    export type WeeklyRecurrenceSelectorProps = AppointmentFormBase.WeeklyRecurrenceSelectorProps;
}

export interface AppointmentFormProps {
    /** Specifies the appointment form's visibility. */
    visible?: boolean;
    /** Handles changes to the appointment form's visibility. */
    onVisibilityChange?: (visible: boolean) => void;
    /** Specifies the appointment's data that the form displays. */
    appointmentData?: AppointmentModel;
    /** Handles changes to the appointment's data. */
    onAppointmentDataChange?: (appointmentData: AppointmentModel) => void;
    /** Specifies the appointment form is read-only. */
    readOnly?: boolean;
    /** An object that specifies localization messages. */
    messages?: AppointmentFormBase.LocalizationMessages;
    /** A component that renders the appointment form's overlay. */
    overlayComponent?: React.ComponentType<AppointmentFormBase.OverlayProps>;
    /** A component that renders the appointment form's layout. */
    layoutComponent?: React.ComponentType<AppointmentFormBase.LayoutProps>;
    /** A component that renders a layout for command buttons. */
    commandLayoutComponent?: React.ComponentType<AppointmentFormBase.CommandLayoutProps>;
    /** A component that renders a layout for editors that edit basic appoinement data. */
    basicLayoutComponent?: React.ComponentType<AppointmentFormBase.BasicLayoutProps>;
    /** A component that renders a layout for editors that specify the appointment's recurrence. */
    recurrenceLayoutComponent?: React.ComponentType<AppointmentFormBase.RecurrenceLayoutProps>;
    /** A component that renders a command button. */
    commandButtonComponent?: React.ComponentType<AppointmentFormBase.CommandButtonProps>;
    /** A component that renders a text editor. */
    textEditorComponent?: React.ComponentType<AppointmentFormBase.TextEditorProps>;
    /** A component that renders a date-time editor. */
    dateEditorComponent?: React.ComponentType<AppointmentFormBase.DateEditorProps>;
    /** A component that renders a text label. */
    labelComponent?: React.ComponentType<AppointmentFormBase.LabelProps>;
    /** A component that renders an editor of Boolean values. */
    booleanEditorComponent?: React.ComponentType<AppointmentFormBase.BooleanEditorProps>;
    /** A component that renders an options menu. */
    selectComponent?: React.ComponentType<AppointmentFormBase.SelectProps>;
    /** A component that renders a radio group. */
    radioGroupComponent?: React.ComponentType<AppointmentFormBase.RadioGroupProps>;
    /** A component that renders a resource editor. */
    resourceEditorComponent?: React.ComponentType<AppointmentFormBase.ResourceEditorProps>;
    /** A component that renders a weekly recurrence selector. */
    weeklyRecurrenceSelectorComponent?: React.ComponentType<AppointmentFormBase.WeeklyRecurrenceSelectorProps>;
}

/** The AppointmentForm plugin renders a form that visualizes appointment's data and allows a user to modify this data. */
export declare const AppointmentForm: React.ComponentType<AppointmentFormProps> & {
    /** A component that renders the appointment form's overlay. */
    Overlay: React.ComponentType<AppointmentFormBase.OverlayProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
    /** A component that renders the appointment form's layout. */
    Layout: React.ComponentType<AppointmentFormBase.LayoutProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
    /** A component that renders a layout for command buttons. */
    CommandLayout: React.ComponentType<AppointmentFormBase.CommandLayoutProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
    /** A component that renders a layout for editors that edit basic appointment data. */
    BasicLayout: React.ComponentType<AppointmentFormBase.BasicLayoutProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
    /** A component that renders a layout for editors that specify the appointment's recurrence. */
    RecurrenceLayout: React.ComponentType<AppointmentFormBase.RecurrenceLayoutProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
    /** A component that renders a text editor. */
    TextEditor: React.ComponentType<AppointmentFormBase.TextEditorProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
    /** A component that renders a date-time editor. */
    DateEditor: React.ComponentType<AppointmentFormBase.DateEditorProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
    /** A component that renders a text label. */
    Label: React.ComponentType<AppointmentFormBase.LabelProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
    /** A component that renders a Boolean value editor. */
    BooleanEditor: React.ComponentType<AppointmentFormBase.BooleanEditorProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
    /** A component that renders an options menu. */
    Select: React.ComponentType<AppointmentFormBase.SelectProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
    /** A component that renders a radio group. */
    RadioGroup: React.ComponentType<AppointmentFormBase.RadioGroupProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
    /** A component that renders a weekly recurrence selector. */
    WeeklyRecurrenceSelector: React.ComponentType<AppointmentFormBase.WeeklyRecurrenceSelectorProps & { className?: string; style?: React.CSSProperties; [x: string]: any }>;
};