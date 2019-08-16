%global packname  extrafont
%global packver   0.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17
Release:          1%{?dist}
Summary:          Tools for using fonts

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-extrafontdb 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rttf2pt1 
Requires:         R-CRAN-extrafontdb 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-Rttf2pt1 

%description
Tools to using fonts other than the standard PostScript fonts. This
package makes it easy to use system TrueType fonts and with PDF or
PostScript output files, and with bitmap output files in Windows.
extrafont can also be used with fonts packaged specifically to be used
with, such as the fontcm package, which has Computer Modern PostScript
fonts with math symbols. See https://github.com/wch/extrafont for
instructions and examples.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
