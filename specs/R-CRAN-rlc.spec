%global __brp_check_rpaths %{nil}
%global packname  rlc
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Interactive Linked Charts with Minimal Code

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jrc >= 0.4.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-hwriter 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-jrc >= 0.4.0
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-hwriter 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-R6 

%description
An easy-to-use tool to employ interactivity in every-day exploratory
analysis. It contains a collection of most commonly used types of charts
(such as scatter plots, line plots, heatmaps, bar charts), which can be
linked to each other or to other interactive elements with just few lines
of code.

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
