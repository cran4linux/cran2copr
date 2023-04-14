%global __brp_check_rpaths %{nil}
%global packname  tukeytrend
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Tukeys Trend Test via Multiple Marginal Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pbkrtest 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-nlme 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-multcomp 
Requires:         R-stats 
Requires:         R-CRAN-pbkrtest 
Requires:         R-mgcv 
Requires:         R-CRAN-lme4 
Requires:         R-nlme 
Requires:         R-Matrix 

%description
Provides wrapper functions to the multiple marginal model function mmm()
of package 'multcomp' to implement the trend test of Tukey, Ciminera and
Heyse (1985) <DOI:10.2307/2530666> for general parametric models.

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
