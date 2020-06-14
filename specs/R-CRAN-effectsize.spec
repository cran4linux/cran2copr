%global packname  effectsize
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Indices of Effect Size and Standardized Parameters

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-insight >= 0.8.4
BuildRequires:    R-CRAN-parameters >= 0.7.0
BuildRequires:    R-CRAN-bayestestR >= 0.6.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-insight >= 0.8.4
Requires:         R-CRAN-parameters >= 0.7.0
Requires:         R-CRAN-bayestestR >= 0.6.0
Requires:         R-stats 
Requires:         R-utils 

%description
Provide utilities to work with indices of effect size and standardized
parameters for a wide variety of models (see support list of insight;
Lüdecke, Waggoner & Makowski (2019) <doi:10.21105/joss.01412>), allowing
computation and conversion of indices such as Cohen's d, r, odds, etc.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
