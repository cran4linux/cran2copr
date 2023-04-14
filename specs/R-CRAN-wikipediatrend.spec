%global __brp_check_rpaths %{nil}
%global packname  wikipediatrend
%global packver   2.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Public Subject Attention via Wikipedia Page View Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-glue >= 1.1.1
BuildRequires:    R-CRAN-stringr >= 0.6.2
BuildRequires:    R-CRAN-httr >= 0.6.1
BuildRequires:    R-CRAN-pageviews >= 0.3.0
BuildRequires:    R-CRAN-rvest >= 0.2.0
BuildRequires:    R-CRAN-xml2 >= 0.1.2
BuildRequires:    R-CRAN-hellno >= 0.0.1
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-glue >= 1.1.1
Requires:         R-CRAN-stringr >= 0.6.2
Requires:         R-CRAN-httr >= 0.6.1
Requires:         R-CRAN-pageviews >= 0.3.0
Requires:         R-CRAN-rvest >= 0.2.0
Requires:         R-CRAN-xml2 >= 0.1.2
Requires:         R-CRAN-hellno >= 0.0.1
Requires:         R-utils 

%description
A convenience wrapper for the Wikipedia page access statistics API binding
the 'pageviews' package and using an additional self composed data source
thus covering a time span from very late 2007 up to the present for daily
page views.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
