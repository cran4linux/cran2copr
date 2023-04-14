%global __brp_check_rpaths %{nil}
%global packname  falcon
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Finding Allele-Specific Copy Number in Next-GenerationSequencing Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1

%description
This is a method for Allele-specific DNA Copy Number Profiling using
Next-Generation Sequencing.  Given the allele-specific coverage at the
variant loci, this program segments the genome into regions of homogeneous
allele-specific copy number.  It requires, as input, the read counts for
each variant allele in a pair of case and control samples. For detection
of somatic mutations, the case and control samples can be the tumor and
normal sample from the same individual.

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
