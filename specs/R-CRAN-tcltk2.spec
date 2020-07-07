%undefine __brp_mangle_shebangs
%global packname  tcltk2
%global packver   1.2-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.11
Release:          3%{?dist}
Summary:          Tcl/Tk Additions

License:          LGPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         tcl >= 8.5
Requires:         tk >= 8.5
BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
Requires:         R-tcltk 

%description
A series of additional Tcl commands and Tk widgets with style and various
functions (under Windows: DDE exchange, access to the registry and icon
manipulation) to supplement the tcltk package

%prep
%setup -q -c -n %{packname}
sed -i 's@/bin/tclsh8.3@/usr/bin/tclsh@g' %{packname}/inst/tklibs/ctext3.2/function_finder.tcl

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/Fonts.txt
%doc %{rlibdir}/%{packname}/gui
%doc %{rlibdir}/%{packname}/po
%doc %{rlibdir}/%{packname}/test.R
%{rlibdir}/%{packname}/tklibs
%{rlibdir}/%{packname}/INDEX
