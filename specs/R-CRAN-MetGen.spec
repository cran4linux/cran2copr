%global __brp_check_rpaths %{nil}
%global packname  MetGen
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Stochastic Weather Generator

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-MASS 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-glmnet 
Requires:         R-MASS 

%description
An adaptation of the multi-variable stochastic weather generator proposed
in 'Rglimclim' to perform gap-filling and temporal extension at sub-daily
resolution. Simulation is performed based on large scale variables and
climatic observation data that could be generated from different gauged
stations having geographical proximity. SWG relies on reanalyses.
Multi-variable dependence is taking into account by using the
decomposition of the product rule (in statistics) into conditional
probabilities. See <https://hal.archives-ouvertes.fr/hal-02554676>.

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
%{rlibdir}/%{packname}
