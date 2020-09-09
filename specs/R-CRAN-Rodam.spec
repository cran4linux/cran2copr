%global packname  Rodam
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Wrapper Functions for 'ODAM' (Open Data for Access and Mining) Web Services

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl >= 1.95
BuildRequires:    R-methods 
Requires:         R-CRAN-RCurl >= 1.95
Requires:         R-methods 

%description
'ODAM' (Open Data for Access and Mining) is a framework that implements a
simple way to make research data broadly accessible and fully available
for reuse, including by a script language such as R. The main purpose is
to make a data set accessible online with a minimal effort from the data
provider, and to allow any scientists or bioinformaticians to be able to
explore the data set and then extract a subpart or the totality of the
data according to their needs. The Rodam package has only one class,
'odamws', that provides methods to allow you to retrieve online data using
'ODAM' Web Services. This obviously requires that data are implemented
according the 'ODAM' approach , namely that the data subsets were
deposited in the suitable data repository in the form of TSV files
associated with their metadata also described in TSV files. See
<http://www.slideshare.net/danieljacob771282/odam-open-data-access-and-mining>.

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
