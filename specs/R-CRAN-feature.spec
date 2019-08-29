%global packname  feature
%global packver   1.2.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.13
Release:          1%{?dist}
Summary:          Local Inferential Feature Significance for Multivariate KernelDensity Estimation

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.4.0
Requires:         R-core >= 1.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ks >= 1.10.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-misc3d 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-stats 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-ks >= 1.10.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-misc3d 
Requires:         R-CRAN-rgl 
Requires:         R-stats 
Requires:         R-tcltk 

%description
Local inferential feature significance for multivariate kernel density
estimation.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
