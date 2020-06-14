%global packname  PearsonICA
%global packver   1.2-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          2%{?dist}
Summary:          Independent component analysis using score functions from thePearson system

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The Pearson-ICA algorithm is a mutual information-based method for blind
separation of statistically independent source signals. It has been shown
that the minimization of mutual information leads to iterative use of
score functions, i.e. derivatives of log densities. The Pearson system
allows adaptive modeling of score functions. The flexibility of the
Pearson system makes it possible to model a wide range of source
distributions including asymmetric distributions. The algorithm is
designed especially for problems with asymmetric sources but it works for
symmetric sources as well.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
