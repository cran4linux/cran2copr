%global packname  PoissonSeq
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Significance analysis of sequencing data based on a Poisson loglinear model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-splines 
Requires:         R-CRAN-combinat 
Requires:         R-splines 

%description
This package implements a method for normalization, testing, and false
discovery rate estimation for RNA-sequencing data. The description of the
method is in Li J, Witten DM, Johnstone I, Tibshirani R (2012).
Normalization, testing, and false discovery rate estimation for
RNA-sequencing data. Biostatistics 13(3): 523-38. We estimate the
sequencing depths of experiments using a new method based on Poisson
goodness-of-fit statistic, calculate a score statistic on the basis of a
Poisson log-linear model, and then estimate the false discovery rate using
a modified version of permutation plug-in method. A more detailed
instruction as well as sample data is available at
http://www.stanford.edu/~junli07/research.html.  In this version, we
changed the way of calculating log foldchange for two-class data. The FDR
estimation part remains unchanged.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
