%global __brp_check_rpaths %{nil}
%global packname  medflex
%global packver   0.6-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.7
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Mediation Analysis Using Natural Effect Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-graphics >= 3.1.2
BuildRequires:    R-stats >= 3.1.2
BuildRequires:    R-utils >= 3.1.2
BuildRequires:    R-CRAN-sandwich >= 2.3.2
BuildRequires:    R-CRAN-car >= 2.0.21
BuildRequires:    R-boot >= 1.3.8
BuildRequires:    R-CRAN-multcomp >= 1.3.6
BuildRequires:    R-Matrix >= 1.1.4
Requires:         R-graphics >= 3.1.2
Requires:         R-stats >= 3.1.2
Requires:         R-utils >= 3.1.2
Requires:         R-CRAN-sandwich >= 2.3.2
Requires:         R-CRAN-car >= 2.0.21
Requires:         R-boot >= 1.3.8
Requires:         R-CRAN-multcomp >= 1.3.6
Requires:         R-Matrix >= 1.1.4

%description
Run flexible mediation analyses using natural effect models as described
in Lange, Vansteelandt and Bekaert (2012) <DOI:10.1093/aje/kwr525>,
Vansteelandt, Bekaert and Lange (2012) <DOI:10.1515/2161-962X.1014> and
Loeys, Moerkerke, De Smet, Buysse, Steen and Vansteelandt (2013)
<DOI:10.1080/00273171.2013.832132>.

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
