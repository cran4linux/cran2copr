%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sansa
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Synthetic Data Generation for Imbalanced Learning in 'R'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ggplot2 

%description
Machine learning is widely used in information-systems design. Yet,
training algorithms on imbalanced datasets may severely affect performance
on unseen data. For example, in some cases in healthcare, financial, or
internet-security contexts, certain sub-classes are difficult to learn
because they are underrepresented in training data. This 'R' package
offers a flexible and efficient solution based on a new synthetic average
neighborhood sampling algorithm ('SANSA'), which, in contrast to other
solutions, introduces a novel “placement” parameter that can be tuned to
adapt to each datasets unique manifestation of the imbalance. More
information about the algorithm's parameters can be found at Nasir et al.
(2022) <https://murtaza.cc/SANSA/>.

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
