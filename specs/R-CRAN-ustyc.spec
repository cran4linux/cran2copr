%global __brp_check_rpaths %{nil}
%global packname  ustyc
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fetch US Treasury yield curve data.

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-plyr 

%description
Forms a query to submit for US Treasury yield curve data, posting this
query to the US Treasury web site's data feed service.  By default the
download includes data yield data for 12 products from January 1, 1990,
some of which are NA during this span.  The caller can pass parameters to
limit the query to a certain year or year and month, but the full download
is not especially large.  The download data from the service is in XML
format.  The package's main function transforms that XML data into a
numeric data frame with treasury product items (constant maturity yields
for 12 kinds of bills, notes, and bonds) as columns and dates as row
names. The function returns a list which includes an item for this data
frame as well as query-related values for reference and the update date
from the service.

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
