%global __brp_check_rpaths %{nil}
%global packname  ExpRep
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Experiment Repetitions

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Allows to calculate the probabilities of occurrences of an event in a
great number of repetitions of Bernoulli experiment, through the
application of the local and the integral theorem of De Moivre Laplace,
and the theorem of Poisson. Gives the possibility to show the results
graphically and analytically, and to compare the results obtained by the
application of the above theorems with those calculated by the direct
application of the Binomial formula. Is basically useful for educational
purposes.

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
