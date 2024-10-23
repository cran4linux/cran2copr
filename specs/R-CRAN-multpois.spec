%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multpois
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Nominal Response Data with the Multinomial-Poisson Trick

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-car >= 3.1.2
BuildRequires:    R-CRAN-plyr >= 1.8.9
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-lme4 >= 1.1.35.5
BuildRequires:    R-CRAN-dfidx >= 0.0.5
Requires:         R-CRAN-car >= 3.1.2
Requires:         R-CRAN-plyr >= 1.8.9
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-lme4 >= 1.1.35.5
Requires:         R-CRAN-dfidx >= 0.0.5

%description
Dichotomous responses having two categories can be analyzed with
stats::glm() or lme4::glmer() using the family=binomial option.
Unfortunately, polytomous responses with three or more unordered
categories cannot be analyzed similarly because there is no analogous
family=multinomial option. For between-subjects data, nnet::multinom() can
address this need, but it cannot handle random factors and therefore
cannot handle repeated measures. To address this gap, we transform nominal
response data into counts for each categorical alternative. These counts
are then analyzed using (mixed) Poisson regression as per Baker (1994)
<doi:10.2307/2348134>. Omnibus analyses of variance can be run along with
post hoc pairwise comparisons. For users wishing to analyze nominal
responses from surveys or experiments, the functions in this package
essentially act as though stats::glm() or lme4::glmer() had a
family=multinomial option.

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
