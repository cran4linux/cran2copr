%global packname  colocalization
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Normalized Spatial Intensity Correlation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 

%description
Calculate the colocalization index, NSInC, in two different ways as
described in the paper (Liu et al., 2019. Manuscript submitted for
publication.) for multiple-species spatial data which contain the precise
locations and membership of each spatial point. The two main functions are
nsinc.d() and nsinc.z(). They provide the Pearson’s correlation
coefficients of signal proportions in different memberships within a
concerned proximity of every signal (or every base signal if single
direction colocalization is considered) across all (base) signals using
two different ways of normalization. The proximity sizes could be an
individual value or a range of values, where the default ranges of values
are different for the two functions.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
