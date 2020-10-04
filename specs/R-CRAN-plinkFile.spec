%global packname  plinkFile
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          'PLINK' (and 'GCTA') File Helpers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch

%description
Provide function that reads binary genotype produced by 'PLINK'
<https://www.cog-genomics.org/plink/1.9/input#bed> into a R matrix, or
scan the genotype one variant at a time like apply(), it also provides
functions that reads and writes genotype relatedness/kinship matrices
created by 'PLINK'
<https://www.cog-genomics.org/plink/1.9/distance#make_rel> or 'GCTA'
<https://cnsgenomics.com/software/gcta/#MakingaGRM>. Currently it does not
support writing back into 'PLINK' binary, it is best used for bringing
data produced by 'PLINK' and 'GCTA' into R environment.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
