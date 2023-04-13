%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quartets
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Datasets to Help Teach Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
In the spirit of Anscombe's quartet, this package includes datasets that
demonstrate the importance of visualizing your data, the importance of not
relying on statistical summary measures alone, and why additional
assumptions about the data generating mechanism are needed when estimating
causal effects. The package includes "Anscombe's Quartet" (Anscombe 1973)
<doi:10.1080/00031305.1973.10478966>, D'Agostino McGowan & Barrett (2023)
"Causal Quartet" <doi:10.48550/arXiv.2304.02683>, "Datasaurus Dozen"
(Matejka & Fitzmaurice 2017), "Interaction Triptych" (Rohrer & Arslan
2021) <doi:10.1177/25152459211007368>, "Rashomon Quartet" (Biecek et al.
2023) <doi:10.48550/arXiv.2302.13356>, and Gelman "Variation and
Heterogeneity Causal Quartets" (Gelman et al. 2023)
<doi:10.48550/arXiv.2302.12878>.

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
