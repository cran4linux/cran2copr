%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  minb
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple-Inflated Negative Binomial Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pscl 
Requires:         R-stats 

%description
Count data is prevalent and informative, with widespread application in
many fields such as social psychology, personality, and public health.
Classical statistical methods for the analysis of count outcomes are
commonly variants of the log-linear model, including Poisson regression
and Negative Binomial regression. However, a typical problem with count
data modeling is inflation, in the sense that the counts are evidently
accumulated on some integers. Such an inflation problem could distort the
distribution of the observed counts, further bias estimation and increase
error, making the classic methods infeasible. Traditional inflated value
selection methods based on histogram inspection are easy to neglect true
points and computationally expensive in addition. Therefore, we propose a
multiple-inflated negative binomial model to handle count data modeling
with multiple inflated values, achieving data-driven inflated value
selection. The proposed approach provides simultaneous identification of
important regression predictors on the target count response as well. More
details about the proposed method are described in Li, Y., Wu, M., Wu, M.,
& Ma, S. (2023) <arXiv:2309.15585>.

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
