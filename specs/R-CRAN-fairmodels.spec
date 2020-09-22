%global packname  fairmodels
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Tool for Bias Detection, Visualization, and Mitigation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-DALEX 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-DALEX 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-scales 

%description
Measure fairness metrics in one place for many models. Check how big is
model's bias towards different races, sex, nationalities etc. Use measures
such as Statistical Parity, Equal odds to detect the discrimination
against unprivileged groups. Visualize the bias using heatmap, radar plot,
biplot, bar chart (and more!). There are various pre-processing and
post-processing bias mitigation algorithms implemented.

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
