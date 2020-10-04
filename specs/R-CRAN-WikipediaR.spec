%global packname  WikipediaR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          R-Based Wikipedia Client

License:          GPL (> 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 2.6.3
BuildRequires:    R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-XML >= 2.6.3
Requires:         R-CRAN-httr >= 1.0.0

%description
Provides an interface to the Wikipedia web application programming
interface (API), using internet connexion.Three functions provide details
for a specific Wikipedia page : all links that are present, all pages that
link to, all the contributions (revisions for main pages, and discussions
for talk pages). Two functions provide details for a specific user : all
contributions, and general information (as name, gender, rights or
groups). It provides additional information compared to others packages,
as WikipediR. It does not need login. The multiplex network that can be
constructed from the results of the functions of WikipediaR can be modeled
as Stochastic Block Model as in Barbillon P., Donnet, S., Lazega E., and
Bar-Hen A. : Stochastic Block Models for Multiplex networks: an
application to networks of researchers, ArXiv 1501.06444,
http://arxiv.org/abs/1501.06444.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
