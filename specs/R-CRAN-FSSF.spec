%global __brp_check_rpaths %{nil}
%global packname  FSSF
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Generate Fully-Sequential Space-Filling Designs Inside a UnitHypercube

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.10

%description
Provides three methods proposed by Shang and Apley (2019)
<doi:10.1080/00224065.2019.1705207> to generate fully-sequential
space-filling designs inside a unit hypercube. A 'fully-sequential
space-filling design' means a sequence of nested designs (as the design
size varies from one point up to some maximum number of points) with the
design points added one at a time and such that the design at each size
has good space-filling properties. Two methods target the minimum pairwise
distance criterion and generate maximin designs, among which one method is
more efficient when design size is large. One method targets the maximum
hole size criterion and uses a heuristic to generate what is closer to a
minimax design.

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
