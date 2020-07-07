%global packname  competitiontoolbox
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          A Graphical User Interface for Antitrust and Trade Practitioners

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-antitrust >= 0.99.11
BuildRequires:    R-CRAN-trade >= 0.5.4
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-antitrust >= 0.99.11
Requires:         R-CRAN-trade >= 0.5.4
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-ggplot2 

%description
A graphical user interface for simulating the effects of mergers, tariffs,
and quotas under an assortment of different economic models. The interface
is powered by the 'Shiny' web application framework from 'RStudio'.

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
