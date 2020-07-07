%global packname  rskey
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          3%{?dist}
Summary:          Create Custom 'Rstudio' Keyboard Shortcuts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-berryFunctions >= 1.17.21
BuildRequires:    R-CRAN-rstudioapi >= 0.5
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-berryFunctions >= 1.17.21
Requires:         R-CRAN-rstudioapi >= 0.5
Requires:         R-graphics 
Requires:         R-utils 

%description
Create custom keyboard shortcuts to examine code selected in the 'Rstudio'
editor. F3 can for example yield 'str(selection)' and F7 open the source
code of CRAN and base package functions on 'github'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/keyboardRlabels.ods
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
