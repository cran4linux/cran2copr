%global packname  ImpactEffectsize
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Calculation and Visualization of the Impact Effect Size Measure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DataVisualizations 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-parallelDist 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-DataVisualizations 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-parallelDist 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 

%description
A non-parametric effect size measure capturing changes in central tendency
or shape of data distributions. The package provides the necessary
functions to calculate and plot the Impact effect size measure between two
groups.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
