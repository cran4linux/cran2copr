%global packname  smerc
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Methods for Regional Counts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-sp 

%description
Implements statistical methods for analyzing the counts of areal data,
with a focus on the detection of spatial clusters and clustering.  The
package has a heavy emphasis on spatial scan methods, which were first
introduced by Kulldorff and Nagarwalla (1995) <doi:10.1002/sim.4780140809>
and Kulldorff (1997) <doi:10.1080/03610929708831995>.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/testdata-raw
%{rlibdir}/%{packname}/INDEX
