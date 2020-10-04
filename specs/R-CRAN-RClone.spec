%global packname  RClone
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Partially Clonal Populations Analysis

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-datasets 
BuildRequires:    R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-datasets 
Requires:         R-methods 

%description
R version of 'GenClone' (a computer program to analyse genotypic data,
test for clonality and describe spatial clonal organization, Arnaud-Haond
& Belkhir 2007,
<http://wwz.ifremer.fr/clonix/content/download/68205/903914/file/GenClone2.0.setup.zip>),
this package allows clone handling as 'GenClone' does, plus the
possibility to work with several populations, MultiLocus Lineages (MLL)
custom definition and use, and p-value calculation for psex statistic
(probability of originating from distinct sexual events) and psex_Fis
statistic (taking account of Hardy-Weinberg equilibrium departure) as
'MLGsim'/'MLGsim2' (a program for detecting clones using a simulation
approach, Stenberg et al. 2003).

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
