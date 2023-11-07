%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  groupTesting
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating and Modeling Group (Pooled) Testing Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-pracma 

%description
Provides an expectation-maximization (EM) algorithm using the approach
introduced in Warasi (2021) <doi:10.1080/03610918.2021.2009867>. The EM
algorithm can be used to estimate the prevalence (overall proportion) of a
disease and to estimate a binary regression model from among the class of
generalized linear models based on group testing data. The estimation
framework we consider offers a flexible and general approach; i.e., its
application is not limited to any specific group testing protocol.
Consequently, the EM algorithm can model data arising from simple pooling
as well as advanced pooling such as hierarchical testing, array testing,
and quality control pooling. Also, provided are functions that can be used
to conduct the Wald tests described in Buse (1982)
<doi:10.1080/00031305.1982.10482817> and to simulate the group testing
data described in Kim et al. (2007)
<doi:10.1111/j.1541-0420.2007.00817.x>.

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
