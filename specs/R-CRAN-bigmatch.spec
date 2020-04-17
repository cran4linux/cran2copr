%global packname  bigmatch
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          Making Optimal Matching Size-Scalable Using Optimal Calipers

License:          MIT+file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rcbalance 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-liqueueR 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-methods 
Requires:         R-CRAN-rcbalance 
Requires:         R-stats 
Requires:         R-CRAN-liqueueR 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mvnfast 
Requires:         R-methods 

%description
Implements optimal matching with near-fine balance in large observational
studies with the use of optimal calipers to get a sparse network. The
caliper is optimal in the sense that it is as small as possible such that
a matching exists. The main functions in the 'bigmatch' package are
optcal() to find the optimal caliper, optconstant() to find the optimal
number of nearest neighbors and nfmatch() to find a near-fine balance
match with a caliper and a restriction on number of nearest neighbors.
Glover, F. (1967).  <DOI:10.1002/nav.3800140304>. Lipski, W., Jr, and
Preparata, F. P. (1981). <DOI:10.1007/BF00264533>. Rosenbaum, P.R. (1989).
<DOI:10.1080/01621459.1989.10478868>. Yang, D., Small, D. S., Silber, J.
H., and Rosenbaum, P. R. (2012). <DOI:10.1111/j.1541-0420.2011.01691.x>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
