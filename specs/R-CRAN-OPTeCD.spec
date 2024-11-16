%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OPTeCD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Partial Tetra-Allele Cross Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Tetra-allele cross often referred as four-way cross or double cross or
four-line cross are those type of mating designs in which every cross is
obtained by mating amongst four inbred lines. A tetra-allele cross can be
obtained by crossing the resultant of two unrelated diallel crosses. A
common triallel cross involving four inbred lines A, B, C and D can be
symbolically represented as (A X B) X (C X D) or (A, B, C, D) or (A B C D)
etc. Tetra-allele cross can be broadly categorized as Complete
Tetra-allele Cross (CTaC) and Partial Tetra-allele Crosses (PTaC).
Rawlings and Cockerham (1962)<doi:10.2307/2527461> firstly introduced and
gave the method of analysis for tetra-allele cross hybrids using the
analysis method of single cross hybrids under the assumption of no
linkage. The set of all possible four-way mating between several genotypes
(individuals, clones, homozygous lines, etc.) leads to a CTaC. If there
are N number of inbred lines involved in a CTaC, the the total number of
crosses, T = N*(N-1)*(N-2)*(N-3)/8. When more number of lines are to be
considered, the total number of crosses in CTaC also increases. Thus, it
is almost impossible for the investigator to carry out the experimentation
with limited available resource material. This situation lies in taking a
fraction of CTaC with certain underlying properties, known as PTaC.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
