%global __brp_check_rpaths %{nil}
%global packname  DNAseqtest
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Generating and Testing DNA Sequences

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Generates DNA sequences based on Markov model techniques for matched
sequences. This can be generalized to several sequences. The sequences
(taxa) are then arranged in an evolutionary tree (phylogenetic tree)
depicting how taxa diverge from their common ancestors. This gives the
tests and estimation methods for the parameters of different models.
Standard phylogenetic methods assume stationarity, homogeneity and
reversibility for the Markov processes, and often impose further
restrictions on the parameters.

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
