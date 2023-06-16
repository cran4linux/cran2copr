%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CIfinder
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate the Confidence Intervals for Predictive Values

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ratesci 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-kableExtra 
Requires:         R-CRAN-ratesci 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-kableExtra 

%description
Computes confidence intervals for the positive predictive value (PPV) and
negative predictive value (NPV) based on varied scenarios. In prospective
studies where the proportion of diseased subjects is an unbiased estimate
of the disease prevalence, this package provides several methods for
calculating the confidence intervals for PPV and NPV including
Clopper-Pearson, Wald, Wilson, Agresti-Coull, and Beta. In situations
where the proportion of diseased subjects does not correspond to the
disease prevalence (e.g. case-control studies), this package provides two
types of solutions: 1) three methods for estimating confidence intervals
for PPV and NPV via ratio of two binomial proportions including Gart & Nam
(1988), Walter (1975), and MOVER-J (Laud, 2017); 2) three direct methods
that compute the confidence intervals including Pepe (2003), Zhou (2007),
and Delta. See the Details and References sections in the corresponding
functions.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
