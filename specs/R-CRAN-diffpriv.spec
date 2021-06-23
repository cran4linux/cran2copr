%global __brp_check_rpaths %{nil}
%global packname  diffpriv
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}%{?buildtag}
Summary:          Easy Differential Privacy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-gsl 
Requires:         R-methods 
Requires:         R-stats 

%description
An implementation of major general-purpose mechanisms for privatizing
statistics, models, and machine learners, within the framework of
differential privacy of Dwork et al. (2006) <doi:10.1007/11681878_14>.
Example mechanisms include the Laplace mechanism for releasing numeric
aggregates, and the exponential mechanism for releasing set elements. A
sensitivity sampler (Rubinstein & Alda, 2017) <arXiv:1706.02562> permits
sampling target non-private function sensitivity; combined with the
generic mechanisms, it permits turn-key privatization of arbitrary
programs.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
