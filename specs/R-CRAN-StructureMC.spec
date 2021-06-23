%global __brp_check_rpaths %{nil}
%global packname  StructureMC
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Structured Matrix Completion

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-MASS 
Requires:         R-CRAN-matrixcalc 

%description
Provides an efficient method to recover the missing block of an
approximately low-rank matrix. Current literature on matrix completion
focuses primarily on independent sampling models under which the
individual observed entries are sampled independently. Motivated by
applications in genomic data integration, we propose a new framework of
structured matrix completion (SMC) to treat structured missingness by
design [Cai T, Cai TT, Zhang A (2016)
<doi:10.1080/01621459.2015.1021005>]. Specifically, our proposed method
aims at efficient matrix recovery when a subset of the rows and columns of
an approximately low-rank matrix are observed. The main function in our
package, smc.FUN(), is for recovery of the missing block A22 of an
approximately low-rank matrix A given the other blocks A11, A12, A21.

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
