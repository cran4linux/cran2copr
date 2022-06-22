%global __brp_check_rpaths %{nil}
%global packname  ipsfs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Intuitionistic, Pythagorean, and Spherical Fuzzy Similarity Measure

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Advanced fuzzy logic based techniques are implemented to compute the
similarity among different objects or items. Typically, application areas
consist of transforming raw data into the corresponding advanced fuzzy
logic representation and determining the similarity between two objects
using advanced fuzzy similarity techniques in various fields of research,
such as text classification, pattern recognition, software projects,
decision-making, medical diagnosis, and market prediction. Functions are
designed to compute the membership, non-membership, hesitant-membership,
indeterminacy-membership, and refusal-membership for the input matrices.
Furthermore, it also includes a large number of advanced fuzzy logic based
similarity measure functions to compute the Intuitionistic fuzzy
similarity (IFS), Pythagorean fuzzy similarity (PFS), and Spherical fuzzy
similarity (SFS) between two objects or items based on their fuzzy
relationships. It also includes working examples for each function with
sample data sets.

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
