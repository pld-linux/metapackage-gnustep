Summary:	GNUStep Suite
Name:		metapackage-gnustep
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Desktop
Requires:	gnustep-base
Requires:	gnustep-gui
Requires:	gnustep-examples
Requires:	WindowMaker
Requires:	GWorkspace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUStep suite metapackage

%files
