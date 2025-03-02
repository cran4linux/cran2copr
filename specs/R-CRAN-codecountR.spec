%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  codecountR
%global packver   0.0.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4.8
Release:          1%{?dist}%{?buildtag}
Summary:          Counting Codes in a Text and Preparing Data for Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Data analysis often requires coding, especially when data are collected
through interviews, observations, or questionnaires. As a result, code
counting and data preparation are essential steps in the analysis process.
Analysts may need to count the codes in a text (Tokenization, counting of
pre-established codes, computing the co-occurrence matrix by line) and
prepare the data (e.g., min-max normalization, Z-score, robust scaling,
Box-Cox transformation, and non-parametric bootstrap). For the Box-Cox
transformation (Box & Cox, 1964, <https://www.jstor.org/stable/2984418>),
the optimal Lambda is determined using the log-likelihood method.
Non-parametric bootstrap involves randomly sampling data with replacement.
Two random number generators are also integrated: a Lehmer congruential
generator for uniform distribution and a Box-Muller generator for normal
distribution. Package for educational purposes.

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
