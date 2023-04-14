%global __brp_check_rpaths %{nil}
%global packname  brandwatchR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          'Brandwatch' API to R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-data.table >= 1.10
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-data.table >= 1.10

%description
Interact with the 'Brandwatch' API
<https://developers.brandwatch.com/docs>. Allows you to authenticate to
the API and obtain data for projects, queries, query groups tags and
categories. Also allows you to directly obtain mentions and aggregate data
for a specified query or query group.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
