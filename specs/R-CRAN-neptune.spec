%global __brp_check_rpaths %{nil}
%global packname  neptune
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          MLOps Metadata Store - Experiment Tracking and Model Registry for Production Teams

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-htmlwidgets >= 1.5.3
BuildRequires:    R-CRAN-reticulate >= 1.22
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-this.path >= 0.4.4
BuildRequires:    R-methods 
Requires:         R-CRAN-plotly >= 4.9.4.1
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-htmlwidgets >= 1.5.3
Requires:         R-CRAN-reticulate >= 1.22
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-this.path >= 0.4.4
Requires:         R-methods 

%description
An interface to Neptune. A metadata store for MLOps, built for teams that
run a lot of experiments. It gives you a single place to log, store,
display, organize, compare, and query all your model-building metadata.
Neptune is used for: • Experiment tracking: Log, display, organize, and
compare ML experiments in a single place. • Model registry: Version,
store, manage, and query trained models, and model building metadata. •
Monitoring ML runs live: Record and monitor model training, evaluation, or
production runs live For more information see <https://neptune.ai/>.

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
