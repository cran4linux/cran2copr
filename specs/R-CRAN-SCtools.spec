%global packname  SCtools
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extensions for Synthetic Controls Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.6.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Synth 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-future >= 1.6.2
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Synth 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-cvTools 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 

%description
Extensions to the synthetic controls analyses performed by the package
'Synth' as detailed in Abadie, Diamond, and Hainmueller (2011) <doi:
10.18637/jss.v042.i13>. Includes generating and plotting placebos,
post/pre-MSPE (Mean Squared Prediction Error) significance tests and
plots, and calculating average treatment effects for multiple treated
units. This package represents an implementation of those methods
suggested in Abadie, Diamond,and Hainmueller (2010)
<doi:10.1198/jasa.2009.ap08746> for use in Synthetic Control Analysis.

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
