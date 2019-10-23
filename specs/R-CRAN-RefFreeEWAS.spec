%global packname  RefFreeEWAS
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          EWAS using Reference-Free DNA Methylation Mixture Deconvolution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-quadprog 

%description
Reference-free method for conducting EWAS while deconvoluting DNA
methylation arising as mixtures of cell types.  The older method (Houseman
et al., 2014,<doi:10.1093/bioinformatics/btu029>) is similar to surrogate
variable analysis (SVA and ISVA), except that it makes additional use of a
biological mixture assumption. The newer method (Houseman et al., 2016,
<doi:10.1186/s12859-016-1140-4>) is similar to non-negative matrix
factorization, with additional constraints and additional utilities.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
