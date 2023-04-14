%global __brp_check_rpaths %{nil}
%global packname  tvgeom
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          The Time-Varying (Right-Truncated) Geometric Distribution

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Probability mass (d), distribution (p), quantile (q), and random number
generating (r and rt) functions for the time-varying right-truncated
geometric (tvgeom) distribution. Also provided are functions to calculate
the first and second central moments of the distribution. The tvgeom
distribution is similar to the geometric distribution, but the probability
of success is allowed to vary at each time step, and there are a limited
number of trials. This distribution is essentially a Markov chain, and it
is useful for modeling Markov chain systems with a set number of time
steps.

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
