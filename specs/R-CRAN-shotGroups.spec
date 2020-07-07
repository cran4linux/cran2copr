%global packname  shotGroups
%global packver   0.7.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5.1
Release:          3%{?dist}
Summary:          Analyze Shot Group Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm >= 1.4.2
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-CompQuadForm >= 1.4.2
Requires:         R-boot 
Requires:         R-CRAN-coin 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-KernSmooth 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Analyzes shooting data with respect to group shape, precision, and
accuracy. This includes graphical methods, descriptive statistics, and
inference tests using standard, but also non-parametric and robust
statistical methods. Implements distributions for radial error in
bivariate normal variables. Works with files exported by 'OnTarget
PC/TDS', 'Silver Mountain' e-target, 'ShotMarker' e-target, or 'Taran', as
well as with custom data files in text format. Supports inference from
range statistics like extreme spread. Includes a set of web-based
graphical user interfaces.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shotGroups_AnalyzeGroups
%doc %{rlibdir}/%{packname}/shotGroups_AngularSize
%doc %{rlibdir}/%{packname}/shotGroups_HitProb
%doc %{rlibdir}/%{packname}/shotGroups_RangeStat
%doc %{rlibdir}/%{packname}/targets_add.rda
%{rlibdir}/%{packname}/INDEX
