%global __brp_check_rpaths %{nil}
%global packname  FastCUB
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Fast EM and Best-Subset Selection for CUB Models for Rating Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-CUB 
Requires:         R-CRAN-Formula 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-CUB 

%description
For ordinal rating data, consider the accelerated Expectation-Maximization
algorithm to estimate and test models within the family of CUB models
(where CUB stands for Combination of a discrete Uniform and a shifted
Binomial distributions). The procedure is built upon Louis' identity for
the observed information matrix.  Best-subset variable selection for CUB
regression models is then implemented on such basis. The methods here
implemented are illustrated and discussed in the preprint available from
Researchgate by Simone R. (2020) <https://tinyurl.com/vvk563e>.

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
%{rlibdir}/%{packname}
