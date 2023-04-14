%global __brp_check_rpaths %{nil}
%global packname  ttbbeer
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          US Beer Statistics from TTB

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch

%description
U.S. Department of the Treasury, Alcohol and Tobacco Tax and Trade Bureau
(TTB) collects data and reports on monthly beer industry production and
operations. This data package includes a collection of 10 years (2006 -
2015) worth of data on materials used at U.S. breweries in pounds reported
by the Brewer's Report of Operations and the Quarterly Brewer's Report of
Operations forms, ready for data analysis. This package also includes
historical tax rates on distilled spirits, wine, beer, champagne, and
tobacco products as individual data sets.

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
