%global __brp_check_rpaths %{nil}
%global packname  overture
%global packver   0.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Writing MCMC

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bigmemory 
Requires:         R-CRAN-bigmemory 

%description
Simplifies MCMC setup by automatically looping through sampling functions
and saving the results.  Reduces the memory footprint of running MCMC and
saves samples to disk as the chain runs.  Allows samples from the chain to
be analyzed while the MCMC is still running.  Provides functions for
commonly performed operations such as calculating Metropolis acceptance
ratios and creating adaptive Metropolis samplers.  References: Roberts and
Rosenthal (2009) <doi:10.1198/jcgs.2009.06134>.

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
