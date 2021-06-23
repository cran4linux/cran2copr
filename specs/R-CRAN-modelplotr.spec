%global __brp_check_rpaths %{nil}
%global packname  modelplotr
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plots to Evaluate the Business Performance of Predictive Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.7
BuildRequires:    R-CRAN-ggfittext >= 0.6.0
BuildRequires:    R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.7
Requires:         R-CRAN-ggfittext >= 0.6.0
Requires:         R-CRAN-rlang >= 0.3.1

%description
Plots to assess the quality of predictive models from a business
perspective. Using these plots, it can be shown how implementation of the
model will impact business targets like response on a campaign or return
on investment. Different scopes can be selected: compare models, compare
datasets or compare target class values and various plot customization and
highlighting options are available. targets like response on a campaign.
Different scopes can be selected: compare models, compare datasets or
compare target class values and various plot customization and
highlighting options are available.

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
