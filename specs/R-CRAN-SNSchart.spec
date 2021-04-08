%global packname  SNSchart
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Normal Scores in Statistical Process Management

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-MASS 

%description
The methods discussed in this package are new non-parametric methods based
on sequential normal scores 'SNS' (Conover et al (2017)
<doi:10.1080/07474946.2017.1360091>), designed for sequences of
observations, usually time series data, which may occur singly or in
batches, and may be univariate or multivariate. These methods are designed
to detect changes in the process, which may occur as changes in location
(mean or median), changes in scale (standard deviation, or variance), or
other changes of interest in the distribution of the observations, over
the time observed. They usually apply to large data sets, so computations
need to be simple enough to be done in a reasonable time on a computer,
and easily updated as each new observation (or batch of observations)
becomes available. Some examples and more detail in 'SNS' is presented in
the work by Conover et al (2019) <arXiv:1901.04443>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
