%global __brp_check_rpaths %{nil}
%global packname  phyreg
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          The Phylogenetic Regression of Grafen (1989)

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides general linear model facilities (single y-variable, multiple
x-variables with arbitrary mixture of continuous and categorical and
arbitrary interactions) for cross-species data. The method is, however,
based on the nowadays rather uncommon situation in which uncertainty about
a phylogeny is well represented by adopting a single polytomous tree. The
theory is in A. Grafen (1989, Proc. R. Soc. B 326, 119-157) and aims to
cope with both recognised phylogeny (closely related species tend to be
similar) and unrecognised phylogeny (a polytomy usually indicates
ignorance about the true sequence of binary splits).

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
