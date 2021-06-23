%global __brp_check_rpaths %{nil}
%global packname  nlstimedist
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Linear Model Fitting of Time Distribution of BiologicalPhenomena

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-minpack.lm >= 1.2.0
BuildRequires:    R-CRAN-nlstools >= 1.0.2
BuildRequires:    R-CRAN-poorman >= 0.2.1
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-minpack.lm >= 1.2.0
Requires:         R-CRAN-nlstools >= 1.0.2
Requires:         R-CRAN-poorman >= 0.2.1
Requires:         R-stats 

%description
Fit biologically meaningful distribution functions to time-sequence data
(phenology), estimate parameters to draw the cumulative distribution
function and probability density function and calculate standard
statistical moments and percentiles. These methods are described in Steer
et al. (2019) <doi:10.1111/2041-210X.13293>.

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
