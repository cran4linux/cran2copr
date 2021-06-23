%global __brp_check_rpaths %{nil}
%global packname  MixAll
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Clustering and Classification using Model-Based Mixture Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-rtkore >= 1.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-methods 
Requires:         R-CRAN-rtkore >= 1.5.0
Requires:         R-methods 

%description
Algorithms and methods for model-based clustering and classification. It
supports various types of data: continuous, categorical and counting and
can handle mixed data of these types. It can fit Gaussian (with diagonal
covariance structure), gamma, categorical and Poisson models. The
algorithms also support missing values. This package can be used as an
independent alternative to the (not free) 'mixtcomp' software available at
<https://massiccc.lille.inria.fr/>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bin
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/lib
%doc %{rlibdir}/%{packname}/makefile
%doc %{rlibdir}/%{packname}/makevars
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/projects
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
